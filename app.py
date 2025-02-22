import sys
import pandas as pd
import streamlit as st
import os
from io import BytesIO

# ======================
# ENVIRONMENT CHECKS
# ======================
try:
    import openpyxl
    from openpyxl.utils.dataframe import dataframe_to_rows
except ImportError:
    st.error("""
    ❗ Missing critical dependencies! Run these commands:
    ```bash
    pip install --upgrade openpyxl pandas streamlit
    pip install --force-reinstall jsonschema-specifications
    ```
    """)
    st.stop()

# ======================
# STREAMLIT APP CONFIG
# ======================
st.set_page_config(page_title="🧾 Data Sweeper", layout='wide')
st.title("🧾 Data Sweeper")
st.write("Transform files between CSV/Excel with data cleaning & visualization!")

# ======================
# FILE PROCESSING
# ======================
uploaded_files = st.file_uploader(
    "Upload files (CSV/Excel):",
    type=["csv", "xlsx"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        with st.expander(f"📁 Processing: {file.name}", expanded=True):
            try:
                # FILE READING
                file_ext = os.path.splitext(file.name)[-1].lower()
                df = pd.DataFrame()

                if file_ext == ".csv":
                    encoding = st.selectbox(
                        f"Select encoding for {file.name}",
                        ["cp1252", "utf-8", "latin1", "ISO-8859-1"],
                        key=f"enc_{file.name}"
                    )
                    df = pd.read_csv(file, encoding=encoding)
                elif file_ext == ".xlsx":
                    df = pd.read_excel(file, engine='openpyxl')
                else:
                    st.error(f"❌ Unsupported file type: {file_ext}")
                    continue

                # FILE METADATA
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("📄 File Details")
                    st.metric("Size", f"{file.size/1024:.2f} KB")
                    st.write(f"**Columns:** {len(df.columns)}")
                    st.write(f"**Rows:** {len(df)}")

                with col2:
                    st.subheader("🔍 Data Preview")
                    st.dataframe(df.head(3), use_container_width=True)

                # DATA CLEANING
                st.subheader("🧹 Data Cleaning")
                if st.checkbox(f"Enable cleaning for {file.name}", key=f"clean_{file.name}"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if st.button(f"Remove duplicates", key=f"dup_{file.name}"):
                            prev_count = len(df)
                            df = df.drop_duplicates()
                            st.success(f"Removed {prev_count - len(df)} duplicates")

                    with col2:
                        if st.button(f"Fill NA values", key=f"fill_{file.name}"):
                            num_cols = df.select_dtypes(include='number').columns
                            df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
                            st.success("Filled numeric missing values")

                # COLUMN MANAGEMENT
                st.subheader("🔧 Column Selection")
                selected_cols = st.multiselect(
                    f"Select columns to keep",
                    df.columns,
                    default=df.columns.tolist(),
                    key=f"cols_{file.name}"
                )
                df = df[selected_cols]

                # VISUALIZATION
                st.subheader("📊 Visualization")
                if st.checkbox(f"Show charts", key=f"viz_{file.name}"):
                    try:
                        num_cols = df.select_dtypes(include='number').columns
                        if len(num_cols) >= 2:
                            st.line_chart(df[num_cols[:2]])
                            st.bar_chart(df[num_cols[:2]])
                        else:
                            st.warning("Need ≥2 numeric columns for visualization")
                    except Exception as e:
                        st.error(f"📈 Visualization error: {str(e)}")
                        st.code("Developer se baat krlo: 03063213951")

                # FILE CONVERSION
                st.subheader("🔄 Format Conversion")
                conversion_type = st.radio(
                    f"Convert to:",
                    ["CSV", "Excel"],
                    horizontal=True,
                    key=f"conv_{file.name}"
                )

                if st.button(f"Convert {file.name}", key=f"btn_{file.name}"):
                    try:
                        buffer = BytesIO()
                        if conversion_type == "CSV":
                            df.to_csv(buffer, index=False, encoding=encoding if file_ext == ".csv" else "utf-8")
                            ext = ".csv"
                            mime = "text/csv"
                        else:
                            df.to_excel(buffer, index=False, engine='openpyxl')
                            ext = ".xlsx"
                            mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        
                        buffer.seek(0)
                        st.download_button(
                            label=f"⬇️ Download {conversion_type}",
                            data=buffer,
                            file_name=file.name.replace(file_ext, ext),
                            mime=mime,
                            key=f"dl_{file.name}"
                        )
                    except Exception as e:
                        st.error(f"❌ Conversion failed: {str(e)}")
                        st.code("Developer se baat krlo: 03063213951")

            except Exception as e:
                st.error(f"⚠️ Critical error processing {file.name}: {str(e)}")
                st.code("Developer se baat krlo: 03063213951")

st.success("✅ All files processed! Apka kaam chal jaega ab.")
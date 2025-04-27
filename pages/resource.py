import streamlit as st
import os
import base64

# 页面配置
st.set_page_config(page_title="LingoNav - 资源中心", page_icon="assert/images/logo.jpg", layout="wide")


# 页面顶部的Logo和导航栏
def header():
    st.markdown("""
        <style>
        .header { 
            background-color: #1E3A8A; 
            padding: 20px; 
            color: white; 
            font-size: 24px;
            text-align: center;
        }
        .nav-bar {
            background-color: #1E3A8A;
            color: white;
            padding: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .nav-links {
            color: white;
            text-decoration: none;
            margin-right: 15px;
        }
        .nav-links:hover {
            text-decoration: underline;
        }
        .resource-box {
            background-color: #f4f4f9;
            border-radius: 10px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .resource-header {
            font-size: 28px;
            color: #1E3A8A;
            font-weight: bold;
            margin-bottom: 15px;
        }
        .resource-item {
            font-size: 18px;
            color: #555;
            line-height: 1.6;
            margin-bottom: 15px;
            padding: 15px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.1);
        }
        .footer {
            background-color: #1E3A8A;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

    # 顶部 Logo 和导航栏
    st.markdown('<div class="header">LingoNav</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="nav-bar">
            <div><a href="#" class="nav-links">首页</a><a href="#" class="nav-links">关于我们</a><a href="#" class="nav-links">产品</a><a href="#" class="nav-links">资源</a></div>
            <div>
                <input type="text" placeholder="搜索" style="padding: 5px;">
                <button>搜索</button>
            </div>
        </div>
    """, unsafe_allow_html=True)


# 资源页面内容
def resource_page():
    st.title("资源中心")

    # 本地PDF文件路径
    pdf_directory = "assert/history"  # PDF文件的本地目录路径
    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

    # 资源列表展示
    st.markdown('<div class="resource-box"><div class="resource-header">词典语料库</div>', unsafe_allow_html=True)

    if not pdf_files:
        st.write("暂无可用资源，请稍后再试。")
    else:
        for pdf_file in pdf_files:
            file_path = os.path.join(pdf_directory, pdf_file)
            file_name = pdf_file.split('.')[0]  # 文件名（不包含扩展名）

            # 将文件内容编码为base64
            with open(file_path, "rb") as f:
                encoded_file = base64.b64encode(f.read()).decode("utf-8")

            # 创建下载链接
            st.markdown(f"""
                <div class="resource-item">
                    <div><strong>资源名称：</strong>{file_name}</div>
                    <div><strong>文件大小：</strong>{os.path.getsize(file_path) // 1024} KB</div>
                    <div>
                        <a href="data:application/pdf;base64,{encoded_file}" download="{pdf_file}" class="nav-links">下载 PDF</a> | 
                        <a href="https://docs.google.com/viewer?url=file://{file_path}" target="_blank" class="nav-links">在线查看</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# 底部信息
def footer():
    st.markdown("""
        <style>
        .footer {
            background-color: #1E3A8A;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="footer">© 2025 LingoNav | <a href="#">反馈意见</a> | <a href="#">网站地图</a></div>',
                unsafe_allow_html=True)


# 主程序
def main():
    header()
    resource_page()
    footer()


if __name__ == "__main__":
    main()

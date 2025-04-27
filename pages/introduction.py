import streamlit as st

# 页面配置
st.set_page_config(page_title="LingoNav - Introduction", page_icon="assert/images/logo.jpg", layout="wide")

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
        .login-status {
            color: white;
            background-color: #FFD700;
            padding: 5px 15px;
            border-radius: 5px;
            cursor: pointer;
        }
        .section-title {
            font-size: 30px;
            font-weight: bold;
            color: #1E3A8A;
            text-align: center;
            margin-top: 40px;
        }
        .section-content {
            font-size: 18px;
            line-height: 1.6;
            margin: 20px;
            text-align: justify;
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
    st.markdown(f"""
        <div class="nav-bar">
            <div><a href="#" class="nav-links">首页</a><a href="#" class="nav-links">关于我们</a><a href="#" class="nav-links">产品</a></div>
            <div>
                <input type="text" placeholder="搜索" style="padding: 5px;">
                <button>搜索</button>
            </div>
            <div>
                <span class="login-status">登录/注册</span>
            </div>
        </div>
    """, unsafe_allow_html=True)


# Introduction 页面内容
def introduction_page():
    # 标题
    st.markdown('<div class="section-title">LingoNav航海外语平台简介</div>', unsafe_allow_html=True)

    # 介绍内容
    st.markdown("""
        <div class="section-content">
        <p><strong>LingoNav航海外语平台</strong>旨在打造一个多语言支持的航运行业语言学习与文化推广平台，以满足航运、航海从业者和爱好者对专业术语学习和跨文化理解的需求。</p>
        <p>我们在初期明确了从教育与培训、文化推广两方面着手，通过多语言词汇学习、文化展示及跨文化交流功能，搭建一个涵盖专业术语、文化认知的多语言生态平台。</p>
        <p>通过LingoNav平台，我们希望能够为航运业的全球化发展、文化传播及多元化合作提供支持。</p>
        <p><strong>我们的愿景是：</strong>立足航海外语，连接全球文化！</p>
        </div>
    """, unsafe_allow_html=True)


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
    introduction_page()
    footer()


if __name__ == "__main__":
    main()

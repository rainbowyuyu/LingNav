import streamlit as st

# 页面配置
st.set_page_config(page_title="LingoNav - About Us", page_icon="assert/images/logo.jpg", layout="wide")


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
        .about-box {
            background-color: #f4f4f9;
            border-radius: 10px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .about-header {
            font-size: 28px;
            color: #1E3A8A;
            font-weight: bold;
            margin-bottom: 15px;
        }
        .about-content {
            font-size: 18px;
            color: #555;
            line-height: 1.6;
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
            <div><a href="#" class="nav-links">首页</a><a href="#" class="nav-links">关于我们</a><a href="#" class="nav-links">产品</a></div>
            <div>
                <input type="text" placeholder="搜索" style="padding: 5px;">
                <button>搜索</button>
            </div>
        </div>
    """, unsafe_allow_html=True)


# About Us页面内容
def about_us_page():
    st.title("关于我们")

    st.markdown("""
        <div class="about-box">
            <div class="about-header">LingoNav团队介绍</div>
            <div class="about-content">
                LingoNav团队由一群来自上海海事大学的热情与创新并存的本科生组成。我们在航运、语言、文化和技术开发等领域具备多元化的背景，致力于构建一个打破语言与文化障碍的全球化平台。
                我们的团队成员来自经济管理、信息工程、徐悲鸿艺术等多个学院专业，每个人都拥有丰富的跨学科知识和实践经验。我们深知全球航运行业对多语言沟通和文化理解的需求，致力于将最新的技术与航运行业的实际需求结合，提供一个既专业又易于使用的语言学习平台。
                通过LingoNav平台，我们希望能够让全球航运从业人员在工作与交流中更加得心应手，促进跨文化沟通，使普通大众也能够了解到航运知识与文化。
            </div>
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
    about_us_page()
    footer()


if __name__ == "__main__":
    main()

import streamlit as st

# 页面标题和蓝色主题
st.set_page_config(page_title="LingNav", page_icon="assert/images/logo.jpg", layout="wide")


# 页面顶部的Logo和导航栏
def header():
    # 检查登录状态
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = None

    # 如果已登录，显示“已登录”，否则显示“登录/注册”
    login_status = f"欢迎：{st.session_state.logged_in}" if st.session_state.logged_in else "登录/注册"

    st.markdown("""
        <style>
        .header { 
            padding: 20px; 
            color: black; 
            font-size: 48px;
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
        </style>
    """, unsafe_allow_html=True)

    # 顶部 Logo 和导航栏
    cola, colb, colc = st.columns([0.2, 2, 0.2])
    with cola:
        st.image("assert/images/logo.jpg", width=240)
    with colb:
        st.markdown('<div class="header">LingNav</div>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="nav-bar">
            <div><a href="#" class="nav-links">首页</a><a href="#" class="nav-links">关于我们</a><a href="#" class="nav-links">翻译</a></div>
            <div>
                <input type="text" placeholder="搜索" style="padding: 5px;">
                <button>搜索</button>
            </div>
            <div>
                <span class="login-status">{login_status}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)


# 显示首页的内容
def home_page():
    st.title("欢迎来到我们的网站")

    col1, col2, col3 = st.columns([0.5,2,0.5])
    with col2:
        # 宣传图
        st.image("assert/images/post.png", use_container_width=True)

    # 使用说明
    st.subheader("使用说明")
    st.markdown("""
        **LingNav**是专为海上行业设计的翻译工具，支持多种语言的实时翻译，帮助船员、港口工作人员等在海上环境中顺畅沟通。

        ## 主要功能
        1. **实时语音翻译**：通过麦克风输入语音，软件会自动识别并翻译成目标语言。适用于需要快速沟通的场景。
        2. **文本翻译**：输入或粘贴文本，软件会自动翻译成目标语言。支持行业专有术语。
        3. **图像翻译**：扫描海上文档或标牌，自动识别并翻译图像中的文字。
        4. **离线翻译**：在没有网络的环境下，您也能使用翻译功能，只需提前下载所需语言包。
        5. **语音播放**：翻译结果支持语音播放，方便用户快速理解翻译内容。
        6. **多语言支持**：支持多种语言，满足全球海上航运的语言需求。
        7. **历史记录与收藏**：保存您的翻译历史，常用短语可收藏，方便再次使用。

        ## 软件界面

        - **主界面**：包含翻译输入框、翻译按钮、语音输入和播放按钮。顶部有语言选择框，右侧是功能按钮。
        - **历史记录**：点击历史记录按钮查看之前翻译过的内容。
        - **设置**：您可以设置默认语言，调整语音播放速度等。

        ## 操作流程
        1. **开始翻译**：选择源语言和目标语言后，点击“翻译”按钮即可开始翻译。
        2. **语音输入**：点击语音按钮，软件会自动识别语音并翻译。
        3. **图像翻译**：点击图像翻译按钮，扫描并翻译图像中的文字。
        4. **离线使用**：通过设置页面下载语言包，启用离线模式。
        5. **查看历史记录**：通过点击“历史记录”按钮，快速查看之前的翻译。
    """)


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

    st.markdown('<div class="footer">© 2025 LingNav | <a href="#">反馈意见</a> | <a href="#">网站地图</a></div>',
                unsafe_allow_html=True)


# 主程序
def main():
    header()
    home_page()
    footer()


if __name__ == "__main__":
    main()

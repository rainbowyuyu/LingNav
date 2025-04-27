import streamlit as st
import asyncio
from googletrans import Translator

# 页面配置
st.set_page_config(page_title="LingoNav - Translate", page_icon="assert/images/logo.jpg", layout="wide")

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


# 异步翻译函数
async def translate_text(translator, text, source_lang, target_lang):
    translation = await translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text


# Translate 子页面内容
def translate_page():
    st.title("在线翻译")

    # 选择源语言和目标语言
    lang_options = ['en', 'zh-cn', 'es', 'fr', 'de', 'it', 'pt', 'ja', 'ko']
    source_lang = st.selectbox("选择源语言", lang_options, index=0)
    target_lang = st.selectbox("选择目标语言", lang_options, index=1)

    # 用户输入待翻译文本
    text_to_translate = st.text_area("输入待翻译文本", "请输入文本...")

    if st.button("翻译"):
        # 使用Google Translate API进行翻译
        if text_to_translate.strip() != "":
            translator = Translator()
            try:
                # 运行异步翻译
                translated_text = asyncio.run(translate_text(translator, text_to_translate, source_lang, target_lang))
                st.success(f"翻译结果：{translated_text}")
            except Exception as e:
                st.error(f"翻译失败：{e}")
        else:
            st.warning("请输入要翻译的文本！")


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
    translate_page()
    footer()


if __name__ == "__main__":
    main()

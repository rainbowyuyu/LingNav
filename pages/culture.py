import streamlit as st

# 页面配置
st.set_page_config(page_title="LingoNav - Culture Resources", page_icon="assert/images/logo.jpg", layout="wide")


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
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .resource-box:hover {
            background-color: #e0e0e0;
        }
        .resource-header {
            font-size: 20px;
            color: #1E3A8A;
            margin-bottom: 10px;
        }
        .resource-description {
            color: #555;
            margin-bottom: 10px;
        }
        .resource-link {
            color: #1E3A8A;
            text-decoration: none;
            font-weight: bold;
        }
        .resource-link:hover {
            text-decoration: underline;
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


# Culture页面内容
def culture_page():
    st.title("文化资源页面")

    st.markdown("""
        在这里，您可以查看与航运行业相关的文化资源文件，包括一些有价值的在线档案馆和海事历史网站。以下是我们精心挑选的一些重要文化资源：
    """)

    # 文化资源列表
    resources = [
        {
            "title": "The National Archives (英国国家档案馆)",
            "description": "提供英国以及世界范围内航运相关的历史档案、政府文件及研究资料，可以深入研究航运历史及相关文化。",
            "link": "https://www.nationalarchives.gov.uk/education/"
        },
        {
            "title": "The Mariners’ Museum (美国海员博物馆)",
            "description": "提供大量关于航运历史、船舶发展以及航海文化的在线资料和展览。",
            "link": "https://www.marinersmuseum.org"
        },
        {
            "title": "Maritime History Virtual Archives (海事历史虚拟档案馆)",
            "description": "这是一个专门收录航海历史的数字资源平台，提供世界各地航运历史的文献和研究资源。",
            "link": "https://www.virginia.edu/maritimehistory/"
        },
        {
            "title": "World Maritime University (世界海事大学)",
            "description": "提供关于航运、海事历史、全球航运文化等方面的研究资料和学术文章，尤其关注全球航运的教育和技术发展。",
            "link": "https://library.wmu.se"
        },
        {
            "title": "Sea History Magazine (海洋历史杂志)",
            "description": "这是一本关于海洋历史的专业杂志，提供航海历史的丰富文章和研究报告，尤其涵盖了航运业的演变。",
            "link": "https://seahistory.org"
        },
        {
            "title": "British Library (英国图书馆)",
            "description": "英国图书馆拥有大量关于航运历史的手稿、档案、书籍等资料，可以访问其数字资源。",
            "link": "https://www.bl.uk"
        }
    ]

    # 显示每个资源
    for resource in resources:
        st.markdown(f"""
            <div class="resource-box">
                <div class="resource-header">{resource['title']}</div>
                <div class="resource-description">{resource['description']}</div>
                <a href="{resource['link']}" class="resource-link" target="_blank">点击访问</a>
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
    culture_page()
    footer()


if __name__ == "__main__":
    main()

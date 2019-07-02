"""生成站点地图相关工具方法
站点地图保存在工程根目录sitemap.xml中，
站点地图文件内容更新是全量更新的，要查询全部文章，
性能和数据库关系较大
"""
import xml.dom.minidom as minidom
from blog.models import Blog, Conf


def generate_sitemap():
    """生成站点地图"""
    # 用于生成sitemap的域名配置读取
    domain_conf = Conf.objects.filter(conf_key='conf_domain').first()
    protocol_conf = Conf.objects.filter(conf_key='conf_protocol').first()
    domain = domain_conf.conf_value
    protocol = protocol_conf.conf_value

    # 查询全部文章并生成站点地图XML文档结构
    blogs = Blog.objects.all()
    sitemap_doc = minidom.Document()
    root = sitemap_doc.createElement("urlset")
    root.setAttribute("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    for blog in blogs:
        node_url = sitemap_doc.createElement("url")
        node_loc = sitemap_doc.createElement("loc")
        node_loc.appendChild(sitemap_doc.createTextNode(protocol + "://" + domain + "/blogs/" + str(blog.pk)))
        node_lastmod = sitemap_doc.createElement("lastmod")
        node_lastmod.appendChild(sitemap_doc.createTextNode(blog.last_modified_time.strftime("%Y-%m-%d")))
        node_url.appendChild(node_loc)
        node_url.appendChild(node_lastmod)
        root.appendChild(node_url)
    sitemap_doc.appendChild(root)
    fp = open("sitemap.xml", "w", encoding="utf-8")
    sitemap_doc.writexml(fp, encoding="utf-8")
    fp.close()

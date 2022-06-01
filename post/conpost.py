from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts

import post as POSTAPI

def post_new_article(title, content,cate,tag,state):
    wp = Client(POSTAPI.SITE+"/xmlrpc.php",POSTAPI.USER,POSTAPI.PASSWORD)
    post = WordPressPost()
    post.title = title
    post.content = content 
    post.post_status = state  # 文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
	

    post.terms_names = {
        'category': cate,#[]
        'post_tag': tag,#[]
    }

    post.id = wp.call(posts.NewPost(post))
    return post.id
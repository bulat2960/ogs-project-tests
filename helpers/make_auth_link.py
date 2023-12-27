def make_auth_link(link, login, password):
    link = list(link)

    link.insert(8, login + ':' + password + '@')
    link = ''.join(map(str, link))
    
    return link
def get_comment(vk_api):
    import vk
    m = vk_api.photos.getComments(photo_id = "456239790")
    m1 = m[len(m)-1]
    if m1["from_id"] == 281141220:
        res = m1["message"]
        return res
    else:
        return 0
        

def build_profile1(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


def build_profile(**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    # user_info['first_name'] = first
    # user_info['last_name'] = last
    return user_info


user_profile1 = build_profile1('albert', 'einstein', location='princeton', field='physics', age=13, height=1.752)
print(user_profile1)
user_profile2 = build_profile(first_name='albert', last_name='einstein', location='princeton', field='physics', age=13,
                              height=1.75)
print(user_profile2)

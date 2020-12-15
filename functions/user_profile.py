"""Sometimes you'll need to use arbitrary keyword arguments, 
so you can write a function that will accept as many key-value pairs 
as the calling statement provides."""
#User profile example
def build_profiles(first, last, **user_info):
    """Dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profiles('Jim','Halpert',
                              location='princeton',
                              field='physics')
print(user_profile)

#instead of **user_info, you'll typically see **kwargs for non-specific keyword arguments (keywordarguments = kwargs)
def build_profile(**kwargs):
    return kwargs

test = build_profile(First = 'Mark', Last = 'Ralph',
              Location = 'TN', Field = 'CS')
print(test)

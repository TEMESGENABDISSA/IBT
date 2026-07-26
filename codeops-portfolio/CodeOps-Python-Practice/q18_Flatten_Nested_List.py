def flatten(lst):
    
    result=[]


    def dfs(items):

        for item in items:

            if isinstance(item,list):

                dfs(item)

            else:

                result.append(item)


    dfs(lst)

    return result
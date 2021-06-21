
"""
Given a function get the list of employees reporting to the hierarchy
"""
lst = []
def get_hierarchy(company_hierarchy, account):
    if not company_hierarchy.get(account):
        return
    else:
        for account in company_hierarchy.get(account):
            lst.append(account)
            get_hierarchy(company_hierarchy, account)
        return (lst)

if __name__=='__main__':
    company_hierarchy = {
        "vice_president": ["director", "ops_manager"],
        "ops_manager": ["ops_developer"],
        "director": ["manager", "senior_manager"],
        "senior_manager": ["engineer"],
        "senior_architect": ["architect"],
        "architect": ["developer"],
        "ceo": [],
    }
    print(get_hierarchy(company_hierarchy=company_hierarchy, account='vice_president'))
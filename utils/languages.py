import pycountry

def country_code_to_name(codes):
    result = []
    for code in codes:
        lang = pycountry.languages.get(alpha_2=code)
        if lang:
            result.append({"code": code, "name": lang.name})
        else:
            result.append({"code": code, "name": code})
    return result
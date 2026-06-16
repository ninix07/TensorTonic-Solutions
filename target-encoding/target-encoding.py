def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    group_count_df={}
    cat_count_df={}
    for i,cat in enumerate(categories):
        group_count_df[cat] = group_count_df.get(cat,0)+targets[i]
        cat_count_df[cat] =  cat_count_df.get(cat,0)+1
    cat_count_df = {cat: group_count_df[cat]/cat_count_df[cat] for cat in group_count_df}
    return [cat_count_df[cat] for cat  in categories]

    
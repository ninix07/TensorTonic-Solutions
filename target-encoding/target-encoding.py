def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    group_count_df={}
    cat_count_df={}
    for i,cat in enumerate(categories):
        group_count_df[cat] = group_count_df.get(cat,0)+targets[i]
        cat_count_df[cat] =  cat_count_df.get(cat,0)+1
    target_encoding= {cat: group_count_df[cat]/cat_count_df[cat] for cat in group_count_df}
    return [target_encoding[cat] for cat  in categories]

    
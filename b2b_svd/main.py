from sklearn.decomposition import TruncatedSVD


def b2b_svd(avg_trxn_amount, num_monthly_trxn):
    new_df = avg_trxn_amount * num_monthly_trxn
    svd = TruncatedSVD(n_components=10, n_iter=10, random_state=42)
    # transposed because you want the top 10 enterprises
    embeddings = svd.fit_transform(new_df.T)
    # embeddings with the max value
    max_enterprise_embeddings = embeddings.argmax(axis=0)
    max_enterprise_rows = new_df.T.iloc[max_enterprise_embeddings]

    return list(max_enterprise_rows.index.values)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



if __name__ == "__main__":
    """
    RSSから取得したニュースを保存
    """
    # これはサンプルプロジェクトなので，ここは適宜変更してください．
    
    ## sample
    file_name = "sample1.txt"

    with open(f"./storage/topic/{file_name}", "w") as f:
        f.write("日経平均株価が9万円台を突破しましたという嘘ニュースのサンプルファイルです．")
    ###
    #
    
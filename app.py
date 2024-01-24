
import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv("final_df_DBSCAN.csv")
st.title('Merchant segmentation Clustering (RFM)')

def Get_Recommendation(User, dataframe):
    Cluster = dataframe[dataframe["User_Id"] == int(User)]["Cluster"].unique()
    if not Cluster:
        st.warning("User not found.")
        return

    Cluster = Cluster[0]
    df_cluster = dataframe[dataframe["Cluster"] == Cluster]
    df_cluster = df_cluster.groupby("Mer_Name")["User_Id"].count().nlargest(5)
    recommendations = list(df_cluster.index)
    
    if recommendations:
            
            recommendations_df = pd.DataFrame({'Recommendations': recommendations})
            recommendations_df.index = np.arange(1, len(recommendations_df) + 1)
            st.table(recommendations_df)

def main():
    User = st.selectbox('Enter User Id:', sorted(df['User_Id'].unique()))
    if st.button("Recommend"):
        Get_Recommendation(User, df)
        

if __name__ == "__main__":
    main()

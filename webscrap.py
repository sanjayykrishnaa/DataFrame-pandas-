import requests
import pandas as pd

cookie = "osano_consentmanager_uuid=3ae0fb04-a114-4f63-8308-d23fe71b60a1; osano_consentmanager=i_3APrAuV9kr0awOItVgO9ePpuGS4al5FQWkGMV5iVA5mIZc_sVJL3f5XhHsmNEtJQ6N57fiTgIJrb1OyIJEVTNdO2A6SlE71jhubvzZJ1hUDZYCRR2SSVQ3UpgPs8PqLzam4avvuGKtCMKUsyH9PPiYWp55NdZTll8gUVAALbEYhv6xvybdkZ7xLFixpzTwk1IkVbD5Fo8UXxe_Br_78SwkbbXQrkrZwbvY1rlIh1m3aXh4i_mNmLsvDSKyskbqGg_XpCz0Fh0BgzvEIVk9hu7eElvBvV63EA_U3g==; _gcl_au=1.1.618818682.1706678528; _fbp=fb.1.1706678528674.109656458; _pin_unauth=dWlkPVpXTXpaakE0WXpFdE56Z3dOUzAwWkdNd0xUazJORE10WmprM1pqa3dNR0prTjJVeg; ajs_anonymous_id=ef5d5239-5588-44f8-8ded-0848575e0d6d; __stripe_mid=e7279bf1-ec24-4cf1-a9e3-734768585708b2f654; _gid=GA1.2.2112499319.1709031464; fw_bid={%22value%22:%22oy79Av%22%2C%22createTime%22:%222024-02-27T10:57:44.397Z%22}; _uetsid=08b63eb0d55f11eea99f5dacf6d573f3; _uetvid=adf09390bff811ee869685498a89c2cd; fw_chid={%22value%22:%22N7A4N3b%22%2C%22createTime%22:%222024-02-27T10:58:57.144Z%22}; _ga_EMDXDP2N4W=GS1.2.1709031464.6.1.1709031538.57.0.0; __cf_bm=JGlg_qMyKxTi2Se473mB_SbAx7f2tZu8ySaUujkqhXg-1709034151-1.0-ATPo0BSLK5aeOkERa+v42hU20fxXWO7zXJeZCcMqD45bRRNbQrZ0W55TOQkEmv+8KkBUi53cfZ+kFGmUn68VrAo=; _gat_UA-000000000-1=1; fw_utm={%22value%22:%22{}%22%2C%22createTime%22:%222024-02-27T11:42:33.181Z%22}; fw_uid={%22value%22:%221a6138d2-a450-4f86-ba48-44601da40ec8%22%2C%22createTime%22:%222024-02-27T11:42:33.210Z%22}; fw_se={%22value%22:%22fws2.93dd1dd0-412d-4453-9d48-7a5f9f25e23c.10.1709034153239%22%2C%22createTime%22:%222024-02-27T11:42:33.239Z%22}; session-prd-tfm=.eJxNT8tygjAA_JecnQ6Jg1ZvVg2GahyVoObCkBBKlJcEq6TTfy_eetjL7uzrB0Rpo0wGpmmcGzUAUa2aIi5V2YJp29x7xihjdFVGbXVVJZgC1fmZ8KTeap8wSyDV_uStJ6FEYdfDSpR_i3xS8zkZkQIXZ3u11O7QOsgKvpAtXcgh1zCjiLnrgD2pt0TbILnSIM9pRwwpQ8tPfhofd3p7Yb1XPjaLzXM99zPuwVr81wsXCu9h-p67QK4rjhMoOzJKVj7kh4eOj9ghl-pJ7cx9ZfTdqM-xAtH6fHymAmGYeFkae9jGr70XyvYoHAYBx4zhW4BnKDwRl9s9Ybhe7hHHHO8v8tCfzjcfSNygOW8-yO3rcYLpKmJ5UDlXHfL3Q2bV3flMboxVEgzA3agm0gmYusPx2HGG8PcPtxKAAw.GL9cKQ.a9dxCNHbdYxOC1KANwEQJlrLnkI; _ga=GA1.1.1452898360.1706678528; _dd_s=rum=0&expire=1709035053509; _ga_2NZ40CS25B=GS1.1.1709034151.11.1.1709034153.58.0.0"

HEADERS={

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie    
}
    
romart_df=pd.read_excel("sanmartt.xlsx",sheet_name="Sheet1")
for i in range(0,len(romart_df)):
    # print(romart_df.loc[i])
    searchterm=romart_df.loc[i]['name']
    # scraptfm=(searchterm)
    URL = f"https://shop.thefreshmarket.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frequency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term={searchterm}"
    responses=requests.get(URL,headers=HEADERS)
    data=responses.json()

    items=data['items'] 
    
    df_items = pd.DataFrame(items)
    cleaned_items_df = df_items[['name', 'base_price']]
    cleaned_items_df.to_excel(f'{searchterm}.xlsx', index=False)
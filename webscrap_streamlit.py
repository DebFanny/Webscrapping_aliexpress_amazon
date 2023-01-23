# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 13:14:16 2023

@author: fanny
"""

import streamlit as st
import pandas as pd
from PIL import Image

import requests
from io import BytesIO

#writing simple text 
data_aliexpress = {'Website': ['AliExpress', 'AliExpress', 'AliExpress', 'AliExpress'],
 'Link': ['https://fr.aliexpress.com/item/1005002954940984.html?spm=a2g0o.productlist.0.0.4cacde9aYWOid1&algo_pvid=21685727-a0a6-443e-994d-050b7fc98450&aem_p4p_detail=20221228105932732939780198220007917803&algo_exp_id=21685727-a0a6-443e-994d-050b7fc98450-4&pdp_ext_f=%7B%22sku_id%22%3A%2212000027804671795%22%7D&pdp_npi=2%40dis%21EUR%217.69%215.77%21%21%21%21%21%402100bdde16722539720031558eaf78%2112000027804671795%21sea&curPageLogUid=QpmhOsyRzPDZ&ad_pvid=20221228105932732939780198220007917803_5&ad_pvid=20221228105932732939780198220007917803_5',
  'https://www.aliexpress.com/item/1005003961163838.html?gps-id=pcDetailBottomMoreThisSeller&scm=1007.13339.291025.0&scm_id=1007.13339.291025.0&scm-url=1007.13339.291025.0&pvid=8ec72d46-2741-4e2e-8851-9f24d2b99ae7&_t=gps-id:pcDetailBottomMoreThisSeller,scm-url:1007.13339.291025.0,pvid:8ec72d46-2741-4e2e-8851-9f24d2b99ae7,tpp_buckets:668%232846%238107%231934&pdp_ext_f=%7B%22sku_id%22%3A%2212000027575278663%22%2C%22sceneId%22%3A%223339%22%7D&pdp_npi=2%40dis%21EUR%213.61%210.09%21%21%21%21%21%400b0a2e9c16740647648072534e6d08%2112000027575278663%21rec',
  'https://www.aliexpress.com/item/1005003172053260.html?gps-id=pcDetailBottomMoreThisSeller&scm=1007.13339.291025.0&scm_id=1007.13339.291025.0&scm-url=1007.13339.291025.0&pvid=d01cf319-c9fd-4ae7-aac3-e73129111a41&_t=gps-id:pcDetailBottomMoreThisSeller,scm-url:1007.13339.291025.0,pvid:d01cf319-c9fd-4ae7-aac3-e73129111a41,tpp_buckets:668%232846%238107%231934&pdp_ext_f=%7B%22sku_id%22%3A%2212000024483133752%22%2C%22sceneId%22%3A%223339%22%7D&pdp_npi=2%40dis%21EUR%213.47%210.09%21%21%21%21%21%400b0a2e9c16740647647912533e6d08%2112000024483133752%21rec',
  'https://www.aliexpress.com/item/1005003735945488.html?gps-id=pcDetailBottomMoreThisSeller&scm=1007.13339.291025.0&scm_id=1007.13339.291025.0&scm-url=1007.13339.291025.0&pvid=d01cf319-c9fd-4ae7-aac3-e73129111a41&_t=gps-id:pcDetailBottomMoreThisSeller,scm-url:1007.13339.291025.0,pvid:d01cf319-c9fd-4ae7-aac3-e73129111a41,tpp_buckets:668%232846%238107%231934&pdp_ext_f=%7B%22sku_id%22%3A%2212000026981218393%22%2C%22sceneId%22%3A%223339%22%7D&pdp_npi=2%40dis%21EUR%217.66%211.81%21%21%21%21%21%400b0a2e9c16740647647912533e6d08%2112000026981218393%21rec'],
 'Product_name': ['Oreiller Long et Doux en forme de Chat 50/70/90/110/130 cm, Jouets en Peluche de Bureau Idéal pour la Sieste, Coussin de Confort pour la Maison, Cadeau Décoratif pour Enfant',
  'Peluche pokémon Pikachu, jouets en peluche mobiles, Kawaii, Eevee, Charmander, carapuce, collection cadeaux, poupée pour garçons et enfants',
  'Chat en peluche doux et mignon de 10 cm, jouet en peluche, pendentif, clé, sac de voiture, suspension, bijoux, cadeau pour enfants',
  "Jouet de Simulation de tigre en peluche pour bébé, peluche douce, Animal sauvage de la forêt, poupée d'oreiller, cadeau d'anniversaire pour enfants, 23cm"],
 'Prices': ['€ 1,68', '€ 0,09', '€ 0,09', '€ 1,81'],
 'Rate': ['4.7', '4.8', '4.9', '4.7'],
 'Number_of_comment': ['307 Avis', '200 Avis', '77 Avis', '103 Avis'],
 'Number_of_sales': ['1682 Commandes',
  '547 Commandes',
  '465 Commandes',
  '685 Commandes'],
 'Estimated_delivry': ['15 fév.', '20 mars.', '20 mars.', '20 mars.'],
 'Picture': ['https://ae01.alicdn.com/kf/H23c266bab9bc4cbcb8a35728ae2e2fc7G/Oreiller-Long-et-Doux-en-forme-de-Chat-50-70-90-110-130-cm-Jouets-en.jpg_Q90.jpg_.webp',
  'https://ae01.alicdn.com/kf/S3086792e834e4857aabffab7fd93033eo/Peluche-pok-mon-Pikachu-jouets-en-peluche-mobiles-Kawaii-Eevee-Charmander-carapuce-collection-cadeaux-poup-e.jpg_Q90.jpg_.webp',
  'https://ae01.alicdn.com/kf/H4b545421face4149bcabc680756a2565J/Chat-en-peluche-doux-et-mignon-de-10-cm-jouet-en-peluche-pendentif-cl-sac-de.jpg_Q90.jpg_.webp',
  'https://ae01.alicdn.com/kf/Hb4bf913507be4dd781169a2432b70aee5/Jouet-de-Simulation-de-tigre-en-peluche-pour-b-b-peluche-douce-Animal-sauvage-de-la.jpg_Q90.jpg_.webp']}
df_aliexpress = pd.DataFrame(data_aliexpress) 

data_amazon = {'Website': ['Amazon'],
 'Link': ['https://www.amazon.fr/Mewaii-Oreiller-danimaux-Mignonne-Moelleux/dp/B0BFV5QMM5/ref=sr_1_51_sspa?keywords=peluche%2Bchat&qid=1674127509&sr=8-51-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfbmV4dA&th=1'],
 'Product_name': ["Mewaii 110CM Peluche Coussin Kawaii Long Oreiller Orange Chat pour Enfant d'animaux Poupée Jouets pour Enfant Mignonne Moelleux Confort Coussins Oreiller en Peluche pour Cadeau 3 Ans et Plus"],
 'Prices': ['45,99€'],
 'Rate': ['4,6 sur 5\xa0étoiles'],
 'Number_of_comment': ['391 évaluations'],
 'Estimated_delivry': ['No information on Availability']}
df_amazon = pd.DataFrame(data_amazon) 

data=df_aliexpress.loc[0]

## Streamlit = API : 
    
st.title("The Place to Buy:  cat Pillow")

image=Image.open(BytesIO(requests.get(data['Picture']).content))
st.markdown("**:red[On AliExpress]** :")
j=0
cols = {}
cols[j], cols[j+1] = st.columns(2)
cols[j].image(image, caption='Product picture',use_column_width= True)


cols[j+1].markdown(f"Product : [{data['Product_name']}]({data['Link']})")
cols[j+1].markdown(f"Prices : {data['Prices']}")
cols[j+1].markdown(f"Average Rate : {data['Rate']} with {data['Number_of_comment']}")
cols[j+1].markdown(f"Number of sales : {data['Number_of_sales']}")
cols[j+1].markdown(f"Estimated delivry : {data['Estimated_delivry']}")

st.markdown("**:red[On Amazon]** :") 

data=df_amazon.loc[0]

## Streamlit = API : 
    
j=400
cols = {}
cols[j], cols[j+1] = st.columns(2)
cols[j].image(image, caption='Product picture',use_column_width= True)


cols[j+1].markdown(f"Product : [{data['Product_name']}]({data['Link']})")
cols[j+1].markdown(f"Prices : {data['Prices']}")
cols[j+1].markdown(f"Average Rate : {data['Rate']} with {data['Number_of_comment']}")
cols[j+1].markdown(f"Estimated delivry : {data['Estimated_delivry']}")


st.markdown("**:blue[Recommanded products]** :")

for i in range(1,4):
    j+=i*4
    cols[j], cols[j+1] = st.columns(2)
    data = df_aliexpress.loc[i]
    image=Image.open(BytesIO(requests.get(data['Picture']).content))
    cols[j].image(image, caption='Product picture',use_column_width= True)
    cols[j+1].markdown(f"{i} - Product : [{data['Product_name']}]({data['Link']})")
    cols[j+1].markdown(f"Prices : {data['Prices']}")
    cols[j+1].markdown(f"Average Rate : {data['Rate']} with {data['Number_of_comment']}")
    cols[j+1].markdown(f"Number of sales : {data['Number_of_sales']}")
    cols[j+1].markdown(f"Estimated delivry : {data['Estimated_delivry']}")






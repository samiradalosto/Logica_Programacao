#Crie uam pasta chamada "projetos"e depois renomeie para 
#"meus_projetos".Por fim,exclua a pasta 

import os 
os.mkdir("nova_pasta")
os.rename("nova_pasta", "meus_projetos")
os.rmdir("meus_projetos")

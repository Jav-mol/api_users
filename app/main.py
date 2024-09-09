from fastapi import FastAPI
from core.config import app as app1

app = FastAPI()
app.include_router(app1)

# Ao5nTK0G2YUTY5tuvn4U5NP+IE0f4PTAMCHSZB0Af5OvM7creKgJBQtvwfFTXb/oczH95v0nlhc2BmScnQ1EeA==

#postgresql://postgres.vevbnctcaosvlnomlrop:Ao5nTK0G2YUTY5tuvn4U5NP+IE0f4PTAMCHSZB0Af5OvM7creKgJBQtvwfFTXb/oczH95v0nlhc2BmScnQ1EeA==@aws-0-sa-east-1.pooler.supabase.com:6543/postgres
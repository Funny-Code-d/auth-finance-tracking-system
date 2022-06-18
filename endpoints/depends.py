from orm.token_map import TokenEntity
from repository.token import TokenRepository



# Token 
def get_token_orm() -> TokenEntity:
    return TokenEntity()

def get_token_repositories() -> TokenRepository:
    return TokenRepository(get_token_orm())
#-----
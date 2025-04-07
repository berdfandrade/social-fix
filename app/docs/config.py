
def docs(description):
    def wrapper(func):
        func.__doc__ = description
        return func
    return wrapper

RouteDescription = {
    "pagina_inicial" : "Retorna a Página de login na rota principal"
}
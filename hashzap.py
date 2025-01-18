# Tela Inicial
   # Titulo: Hashzap
   # Botão:  Inicial chat
      # quando clicar no botão:
      # abrir um popup/modal/alerta
          # Título: Bem vindo Hashzap
          # Caixa de Texto: Escreva seu nome no chat
          # Botão: Entrar no chat 
             # quando clicar no botão
             # sumir com o título 
             # sumir  com o botão Iniciar Chat
                # carregar o chat
                # carregar o campo de enviar mensagem: "Digite a sua mensagem"
                # botão Enviar
                    # quando clicar no botão enviar
                    # enviar a mensagem
                    # limpar a caixa de mensagem
                        
# flet
# importar o flet
import flet as ft

# criar uma função principal para rodar o seu aplicativo 
def main(pagina):
   # titulo 
   titulo = ft.Text("Hashzap")
   
   campo_enviar_mensagem = ft.TextField(label="Digite aqui a sua mensagem")
   botao_eviar = ft.ElevatedButton("Enviar")
   
   def entrar_chat(evento):
      popup.open = False
      pagina.remove(titulo)
      pagina.remove(botao)
      pagina.add(campo_enviar_mensagem)
      pagina.add(botao_eviar)
      pagina.update()
   
   # criar o popup
   titulo_popup = ft.Text("Bem vindo ao Hashzap")
   caixa_nome = ft.TextField(label="Digite o seu nome")
   botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
   
   popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])
   
   def abrir_popup(evento):
      pagina.dialog = popup
      popup.open = True
      pagina.update()
      print("clicou no botão")
   
   # botão incial 
   botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
   
   pagina.add(titulo)
   pagina.add(botao)
   

ft.app(main, view=ft.WEB_BROWSER)

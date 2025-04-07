import obspython as obs
import os

vitorias = 0
derrotas = 0
score_path = "C:/Users/thiag/Documents/contador obs/score.txt"

def atualizar_score():
    with open(score_path, "w") as f:
        f.write(f"W:{vitorias} | L:{derrotas}")


def add_vitoria(props, button):
    global vitorias
    vitorias += 1
    atualizar_score()

def add_derrota(props, button):
    global derrotas
    derrotas += 1
    atualizar_score()

def resetar_placar(props, button):
    global vitorias, derrotas
    vitorias = 0
    derrotas = 0
    atualizar_score()

def script_description():
    return "Central win/loss scoreboard: '3 – 1' style"

def script_update(settings):
    atualizar_score()

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, "btn_vitoria", "Adicionar Vitória", add_vitoria)
    obs.obs_properties_add_button(props, "btn_derrota", "Adicionar Derrota", add_derrota)
    obs.obs_properties_add_button(props, "btn_reset", "Resetar Placar", resetar_placar)
    return props

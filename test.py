from enemys import Goblin, Boss, Skeleton
from heros import Hero
from Attacks import attack, aoe_attack, lightning_orb, chain_lightning, fireball, firewall
from game_functions import stats, enemy_spawner, hero_chose_attack, use_items

round = 3
alive_enemys = []
enemy_spawner(round, alive_enemys)

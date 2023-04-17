from classes.arena.base_singltone import BaseSingleton

from typing import Optional

from classes.units.enemy import Enemy
from classes.units.player import Player


class Arena(metaclass=BaseSingleton):
    """
    Класс арены
    """
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False

    def start_game(self, player: Player, enemy: Enemy) -> None:
        """
        Функция для старта игры
        """
        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    def battle_result(self) -> Optional[str]:
        """
        Функция для вывода результата игры в случае победы одного из игроков
        """
        player_hp = self.player.health_points
        enemy_hp = self.enemy.health_points

        if player_hp == 0 and enemy_hp == 0:
            return f'{self.player.name} и {self.enemy.name} погибают в бою, бой завершился НИЧЬЕЙ!'
        elif player_hp == 0:
            return f"{self.player.name} погибает в бою, побеждает {self.enemy.name}"
        elif enemy_hp == 0:
            return f"{self.enemy.name} погибает в бою, побеждает {self.player.name}"
        else:
            return None

    def _stamina_regeneration(self) -> None:
        """
        Функция пополнения запаса выносливости после каждого хода
        """
        self.player.add_stamina(self.STAMINA_PER_ROUND)
        self.enemy.add_stamina(self.STAMINA_PER_ROUND)

    def enemy_hit(self) -> str:
        """
        Функция хода соперника
        """
        result = self.enemy.hit(self.player)
        self._stamina_regeneration()
        return result

    def end_game(self) -> None:
        """
        Функция окончания игры
        """
        self._instances = {}
        self.game_is_running = False

    def player_hit(self) -> str:
        """
        Функция хода игрока
        """
        result = self.player.hit(self.enemy)
        self._stamina_regeneration()
        return result

    def player_use_skill(self) -> str:
        """
        Функция применения навыка игроком
        """
        result = self.player.use_skill(self.enemy)
        self._stamina_regeneration()
        return result

    def player_pass(self):
        """
        Функция пропуска хода игроком
        """
        self._stamina_regeneration()
        return f'{self.player.name} пропустил ход. '

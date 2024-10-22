"""Contains the MW3 schema."""

from pydantic import BaseModel, Field


# Weapons
class Weapon(BaseModel):
    """The MW3 weapon schema."""

    name: str
    level: int = 1


class AssaultRifles(BaseModel):
    """The MW3 AR schema."""

    SVA_545: Weapon = Field(alias="SVA 545", default=Weapon(name="SVA 545"))


class BattleRifles(BaseModel):
    """The MW3 AR schema."""

    BAS_B: Weapon = Field(alias="BAS-B", default=Weapon(name="BAS-B"))


class SMGs(BaseModel):
    """The MW3 SMGs schema."""

    STATIC_HV: Weapon = Field(alias="Static-HV", default=Weapon(name="Static-HV"))


class Weapons(BaseModel):
    """The MW3 weapons schema."""

    assault_rifles: AssaultRifles = Field(
        alias="Assault Rifles", default=AssaultRifles()
    )
    battle_rifles: BattleRifles = Field(alias="Battle Rifles", default=BattleRifles())
    smgs: SMGs = Field(alias="SMGs", default=SMGs())


# Base
class MW3(BaseModel):
    """The MW3 schema."""

    level: int = 1
    weapons: Weapons = Weapons()

extends Node2D

func _ready() -> void:
	Wwise.register_game_obj(self, self.name)
	Wwise.register_listener(self)
	Wwise.load_bank_id(AK.BANKS.DCP_THE_CORE)
	Wwise.load_bank_id(AK.BANKS.MAIN)
	Wwise.load_bank_id(AK.BANKS.MUSIC)
	Wwise.post_event_id(AK.EVENTS.DEFEATED_BAUUL, self)

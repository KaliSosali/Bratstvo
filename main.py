from cfgmanager import Config
import recognition, actions, immitate

def main():
	cfg = Config("config.json")
	for text in recognition.start_listening(cfg):
		print("Input: " + text)
		result = actions.convert_to_action(text, cfg)
		print("Doing: " + result)
		immitate.execute_input(result)

if __name__ == "__main__":
	main()
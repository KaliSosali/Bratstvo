from cfgmanager import Config
import recognition, actions, immitate

def main():
    cfg = Config("config.json")

    skills = list(cfg.get("skills"))
    heroes = list(cfg.get("heroes"))
    words = ["[unk]"]

    for word in skills:
        words.insert(0, word)
    for word in heroes:
        words.insert(0, word)

    for output in recognition.start_listening(cfg, words):
        if output[0] == "partial":
            continue
        text = output[1]
        print("Input: " + text)
        result = actions.convert_to_action(text, cfg)
        if result:
            print("Doing: " + result)
            immitate.execute_input(result)

if __name__ == "__main__":
	main()

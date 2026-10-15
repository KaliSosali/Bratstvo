def convert(cmd, cfg):
	to_convert = cmd.split()

	heroes_dict = cfg.get("heroes")
	boys = list(heroes_dict) #only keys(names)

	skills_dict = cfg.get("skills")
	skills = list(skills_dict)

	todo = "" #Convert result

	for command in to_convert: #Throw everything into a pile so we can sort it out later
		if command in boys:
			todo += heroes_dict[command]
			continue
		if command in skills:
			todo += skills_dict[command]


	poof_bind = skills_dict[skills[0]]
	all_units_bind = heroes_dict[boys[0]]
	all_other_units_bind = heroes_dict[boys[1]]


	replace_phrases = {
		all_units_bind + poof_bind : f"@{poof_bind}{poof_bind}",
		all_other_units_bind + poof_bind : f"@{poof_bind}"
	}
	

	for phrase in list(replace_phrases):
		todo = todo.replace(phrase, replace_phrases[phrase])

	return todo

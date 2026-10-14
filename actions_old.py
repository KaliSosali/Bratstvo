def convert_to_action(cmd, cfg):
	heroes_dict = cfg.get("heroes")
	bratstvo = list(heroes_dict) #берем тока ключи

	skills_dict = cfg.get("skills")
	skills = list(skills_dict)


	workers = [] #Выполняющие
	action = '' #Действие выполняющих

	todo = "" #Список для клавиш, которые будем нажимать

	for brat in bratstvo:
		if brat in cmd:
			workers.append(brat)
			if brat == bratstvo[0]:
				break #Выходим из цикла если есть команда выбора всех сущностей
			
	if not workers:
		return '' #Если в перреданой команде нет имен - выходим

	for skill in skills:
		if skill in cmd:
			action = skill
			break #Два действия? берем первое

	#Если нету действий - ничего страшного

	#Конвертим все в клавиши
	if not action:
		todo = heroes_dict[workers[0]] # Нету действия? просто селектим первого названого/всю братву
		return todo

	if action == skills[0]:
		if bratstvo[0] in workers:
			todo = "ctrl+" + skills_dict[action] + " " + skills_dict[action] #Если пуфаеться вся братва, пуфаемся через контрл и еще один обычный пуф(для мейна)
		else:
			for brat in workers:
				todo += heroes_dict[brat] + skills_dict[action] #Иначе пуфаемся по одному: brat1wbrat2w

	else:
		todo = heroes_dict[workers[0]] + skills_dict[action] #Если не пуф - просто берем первого названого и делаем что сказали

	return todo

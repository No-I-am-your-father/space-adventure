# coding=utf-8

# Space Exploration: A Text-based Adventure Game
# (Version 1.0)

import random

def msg(location):
    if location['msg'] == '':
        return '\n'+'You are at '+location['name']+'.'+'\n'+'Status: '+'\n'+location['status']
    else:
        return location['msg']

def get_choice(location,dir):
    if dir=='f':
        choice = 0
    elif dir=='b':
        choice = 1
    elif dir=='r':
        choice = 2
    elif dir=='l':
        choice = 3
    else:
        return -1
    
    if location['directions'][choice] == 0:
        return 4
    else:
        return choice

def main():
    dirs = (0,0,0,0) # Default directions
    
    # Locations
    darwin = {'name':'Darwin the Terrestrial Planet','directions':dirs,'msg':'','status':''}
    newton_leibniz = {'name':'Newton-Lebniz the Double Planet','directions':dirs,'msg':'','status':''}
    leeuwenhoek = {'name':'Leeuenhoek the Dwarf Planet','directions':dirs,'msg':'','status':''}
    bartholin = {'name':'Barth the City Planet','directions':dirs,'msg':'','status':''}
    sagan = {'name':'Sagan the Ice Planet','directions':dirs,'msg':'','status':''}
    cuvier = {'name':'Cuvier the Ocean Planet','directions':dirs,'msg':'','status':''}
    hawking = {'name':'Hawking the Silicate Planet','directions':dirs,'msg':'','status':''}
    huygens = {'name':'Huygens the Gas Giant','directions':dirs,'msg':'','status':''}
    roemer = {'name':'Roemer the G-Type Star','directions':dirs,'msg':'','status':''}
    curie = {'name':'Curie the Neutron Star','directions':dirs,'msg':'','status':''}
    wasp_hive = {'name':'the Wasp Hive the asteroid belt','directions':dirs,'msg':'','status':''}
    higgs = {'name':'the Higgs Field - empty space, or is it?','directions':dirs,'msg':'','status':''}
    jemison = {'name':'Jemison District - just empty space','directions':dirs,'msg':'','status':''}
    hollingworth = {'name':'Hollingworth District - just empty space','directions':dirs,'msg':'','status':''}
    tu = {'name':'Tu Memorial Space - just empty space','directions':dirs,'msg':''}
    dark_unknown = {'name':'an unknown area - it\'s dark out here','directions':dirs,'msg':'','status':''}
    rogue = {'name':'an unidentified planet','directions':dirs,'msg':'','status':''}

    # Directions
    darwin['directions'] = (dark_unknown,higgs,0,leeuwenhoek)
    newton_leibniz['directions'] = (wasp_hive,cuvier,hollingworth,0)
    leeuwenhoek['directions'] = (tu,roemer,darwin,rogue)
    bartholin['directions'] = (higgs,0,0,hawking)
    sagan['directions'] = (curie,tu,0,0)
    cuvier['directions'] = (newton_leibniz,0,sagan,tu)
    hawking['directions'] = (roemer,hollingworth,bartholin,wasp_hive)
    huygens['directions'] = (0,jemison,leeuwenhoek,0)
    roemer['directions'] = (leeuwenhoek,hawking,higgs,jemison)
    curie['directions'] = (hollingworth,sagan,0,cuvier)
    wasp_hive['directions'] = (jemison,newton_leibniz,hawking,0)
    higgs['directions'] = (darwin,bartholin,0,roemer)
    jemison['directions'] = (rogue,wasp_hive,roemer,0)
    hollingworth['directions'] = (hawking,curie,0,newton_leibniz)
    tu['directions'] = (sagan,leeuwenhoek,dark_unknown,huygens)
    dark_unknown['directions'] = (0,darwin,cuvier,tu)
    rogue['directions'] = (huygens,jemison,leeuwenhoek,0)

    # Status (additional text to accompagny the location names)
    darwin['status'] = 'Oxygen level: 43%'+'\n'+'Temperature: 24 degrees celsius'+'\n'+'Water: Some'+'\n'+'Food: Some'+'\n'+'Habited: No'
    newton_leibniz['status'] = 'Oxygen level: 15%'+'\n'+'Temperature: 16 degrees celsius'+'\n'+'Water: None'+'\n'+'Food: None'+'\n'+'Habited: No'
    leeuwenhoek['status'] = 'Oxygen level: 22%'+'\n'+'Temperature: 42 degrees celsius'+'\n'+'Water: Limited'+'\n'+'Food: Limited'+'\n'+'Habited: No,but there seems to be an abandoned research station.'
    bartholin['status'] = 'You are no longer welcome at this planet.'
    sagan['status'] = 'Oxygen level: 13%'+'\n'+'Temperature: -12 degrees celsius'+'\n'+'Water: Some'+'\n'+'Food: Limited'+'\n'+'Habited: Yes, and the species seems to be hostile!'
    cuvier['status'] = 'Oxygen level: 18%'+'\n'+'Temperature: 9 degrees celsius'+'\n'+'Water: There\'s nothing BUT water here'+'\n'+'Food: Plenty'+'\n'+'Habited: Yes'
    hawking['status'] = 'Oxygen level: 23%'+'\n'+'Temperature: 36 degrees celsius'+'\n'+'Water: Some'+'\n'+'Food: Limited'+'\n'+'Habited: No.'
    huygens['status'] = 'This is not a planet.'
    roemer['status'] = 'If you get any nearer, this sun will burn you up!'
    curie['status'] = '* WARNING: EXTREME RADIATION LEVELS! *'+'\n'+'Oxygen level: 4%'+'\n'+'Temperature: 53 degrees celsius'+'\n'+'Water: Limited'+'\n'+'Food: None'+'\n'+'Habited: No'
    wasp_hive['status'] = 'This is not a planet.'
    higgs['status'] = 'This is not a pla - LOOK OUT! - those asteroids are everywhere!'
    jemison['status'] = 'This is not a planet.'
    hollingworth['status'] = 'This is not a planet.'
    tu['status'] = 'This is not a planet.'
    dark_unknown['status'] = 'If something\'s hiding out here, we sure can\'t see it.'
    rogue['status'] = 'This planet is rogue. You can\'t live here.'

    # Random planets that might make a suitable home
    habitable_planets = [darwin,leeuwenhoek,cuvier,hawking]
    new_home_planet = random.choice(habitable_planets)

    # Position (changes value once the player moves)
    location = bartholin

    # Game intro
    print('\n'+'* * * * * * * * * * SPACE EXPLORATION * * * * * * * * * *'+'\n')
    print('The year is 3042. You\'ve been banished from your home planet - the planet Barth. '+'\n'+'Now it\'s just you and your astrobiologist pal ... '+'\n'+'(Please enter the name of your pal)')
    pal_name = raw_input()
    print('... the magnificent turtle in your starship ...'+'\n'+'(Please enter the name of your starship)')
    starship_name = raw_input()
    print('... flying off into space, in search of a new home planet.'+'\n'+'\n'+starship_name+' can fly in four directions: Forwards, backwards, right and left.'+'\n')

    # Game loop
    while True:
        if location['name'] == new_home_planet['name']:
            print(msg(location))
            print('\n'+pal_name+': I\'ve run my tests and this planet seems suitable for living, let\'s settle down here!')
            break
        elif location['name'] == bartholin['name']:
            print(msg(location))
            print('\n'+'You better get away from here!') # When the player visits the planet Barth
        else:
            print(msg(location))
            print('\n'+pal_name+': I don\'t think this place will do. Let\'s move on.')
        
        stuck = True
        while stuck:
            print('')
            dir = input('Which direction do you want to go: f, b, r or l? ')
            choice = get_choice(location,dir)
            if choice == -1:
                print('Please enter f, b, r or l ')
            elif choice == 4:
                print('You cannot fly in that direction, that would be suicide!')
            else:
                location = location['directions'] [choice]
                stuck = False

main()

# The location names in this game were inspired by;
# 
# Antonie van Leeuwenhoek, microscopist and microbiologist
# Carl Sagan, astronomer, cosmologist, astrophysicist and -biologist
# Caspar Bartholin the Elder & sons, physicians et al.
# Charles Darwin, biologist, geologist and naturalist
# Christiaan Huygens, astonomer, mathematician and physicist
# Georges Cuvier, naturalist and zoologist
# Gottfried W. Leibniz, logician, mathematician and philosopher
# Isaac Newton, astronomer, mathematician, physicist and theologian
# Leta Hollingworth, psychologist
# Mae Jemison, astronaut, engineer and physician
# Marie Curie, chemist and physicist
# Ole Rømer, astronomer
# Peter Higgs, theoretical physicist
# Stephen Hawking, cosmologist and theoretical physicist
# Tu Youyou, pharmaceutical chemist

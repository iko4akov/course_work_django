def fill(list_essence: list, object_esse):
    essence_for_create = []

    for items in list_essence:
        essence_for_create.append(object_esse(**items))

    object_esse.objects.bulk_create(essence_for_create)

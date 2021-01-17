def has_cycle(head):
    if head is None:
        return False
    
    track = head
    passed = []

    while track is not None:
        if track not in passed:
            passed.append(track)
        else:
            return True
        track = track.next
    
    return False
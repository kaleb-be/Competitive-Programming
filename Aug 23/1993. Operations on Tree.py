class LockingTree:
    def __init__(self, parent):
        self.parent = parent
        self.n = len(parent)
        self.locked = [False] * self.n
        self.user = [-1] * self.n
        self.children = [[] for _ in range(self.n)]

        for i in range(1, self.n):
            self.children[parent[i]].append(i)

    def lock(self, num, user):
        if not self.locked[num]:
            self.locked[num] = True
            self.user[num] = user
            return True
        return False

    def unlock(self, num, user):
        if self.locked[num] and self.user[num] == user:
            self.locked[num] = False
            self.user[num] = -1
            return True
        return False

    def upgrade(self, num, user):
        if not self.locked[num] and self.hasLockedDescendant(num) and not self.hasLockedAncestor(num):
            self.locked[num] = True
            self.user[num] = user
            self.unlockDescendants(num)
            return True
        return False

    def hasLockedDescendant(self, num):
        for child in self.children[num]:
            if self.locked[child] or self.hasLockedDescendant(child):
                return True
        return False

    def hasLockedAncestor(self, num):
        while num != -1:
            if self.locked[num]:
                return True
            num = self.parent[num]
        return False

    def unlockDescendants(self, num):
        for child in self.children[num]:
            self.unlockDescendants(child)
            self.locked[child] = False
            self.user[child] = -1


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
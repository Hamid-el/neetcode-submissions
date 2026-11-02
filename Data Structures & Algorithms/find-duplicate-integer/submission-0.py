class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        
        while True:
            slow = nums[slow] # random jumping, but with the doppelte zahl, there will be granteed to have a cycle
            fast = nums[nums[fast]] # fast will also evantually be part of that cycle

            if slow == fast:
                break

        # find beginning of cycle. fast took |slow|-many steps um an curr punkt zu kommen, daher können wir slow wieder anfang packen
        # cycle beginns t doppelte zahl
        # wenn zb slow 3 schritte gemacht hat, dann hst fast 6 gemacht
        #slow in erste schleife macht immer k*anzhl cyclus runden schritte bis es fast trifft # und slow anzahl an schritte ist vielfaches von 1 cycle runde
        # slow und fast treffen nicht immer an zyklenanfang!
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
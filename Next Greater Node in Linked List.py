class solution:
   def nextargerNodes(self, head: Optional[ListNode]) -> List[int]:
      lst = []
      while head:
         lst.append(head.val)
         head = head.next
      i = 0
      l = len(lst)
      ans = [0] * l
      tmp = []
      while i < l:
         while tmp and lst[tmp[-1]] < lst[i]:
            ans[tmp[-1]] = lst[i]
            tmp.pop()
         tmp.append(i)
         i += 1
      return ans

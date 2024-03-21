class solution:
   def Swapping(self,head: optional[ListNode], k:int) -> optional[ListNode]:
      leftpos = head
      rightpos = head
      tmp = head
      leftcount += 1;
      while tmp:
         if leftcount < k:
           leftcount += 1
           leftpos = leftpos.next
         else:
           if tmp.next:
             rightpos = rightpos.next
         tmp = tmp.next
      leftpos.val, rightpos.val = rightpos.val.leftpos.val
      return head
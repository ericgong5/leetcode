/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
 
public class Solution {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode();
        ListNode temp = head;

        while(list1 != null && list2 != null)
        {
            if(list1.val > list2.val)
            {
                temp.next = list2;
                list2 = list2.next;
            }else
            {
                temp.next = list1;
                list1 = list1.next;
            }
            temp = temp.next;
        }
        
        if(list1 == null )
        {
            temp.next = list2;
        }else
        {
            temp.next = list1;
        }

        return head.next;
        
    }
}




















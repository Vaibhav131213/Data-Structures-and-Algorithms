// Problem: Reverse Linked List
// Link: https://leetcode.com/problems/reverse-linked-list/

class ListNode {
    int val;
    ListNode next;
    ListNode(int x){val=x;}
}

public class ReverseLinkedList {
    public ListNode reverseList(ListNode head){
        ListNode prev=null, curr=head;
        while(curr!=null){
            ListNode nxt=curr.next;
            curr.next=prev;
            prev=curr;
            curr=nxt;
        }
        return prev;
    }

    public static void main(String[] args){
        ListNode a=new ListNode(1);
        a.next=new ListNode(2);
        a.next.next=new ListNode(3);
        ListNode rev=new ReverseLinkedList().reverseList(a);
        while(rev!=null){
            System.out.print(rev.val+" "); // 3 2 1
            rev=rev.next;
        }
    }
}

// Last Updated: 2/5/2026, 9:25:24 AM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    
    if(head!=NULL)
    {
    struct ListNode* prev=head;
    struct ListNode* curr=head->next;
    struct ListNode* temp=NULL;
    while(curr!=NULL&& head!=NULL)
    {
        if(prev->val==curr->val)
        {
            temp=curr;
            prev->next=curr->next;
            curr=curr->next;
        }
        else{
            prev=prev->next;
            curr=curr->next;
        }

    }
    return head;
    
    }
    return head;
    
}
import unit4.collectionsLib.*;

public class Work
{
    //The operation receives a binary tree and a node in the tree, the operation
    //Returns the parent of son, null if son
    //He is the root of the tree or the tree is empty
    public static BinNode<Integer> parent(BinNode<Integer> tr, BinNode<Integer> son)//Q28
    {
        if (tr == null || son == null)
            return null;
        if (tr.getLeft() == son || tr.getRight() == son)
            return tr;
        BinNode<Integer> left = parent(tr.getLeft(), son);
        if (left != null)
            return left;
        return parent(tr.getRight(), son);
    }


    //The operation receives two nodes in a binary tree and returns 'true' if they are siblings, 'false' - otherwise.
    // Assumption:: tr is not empty and son2,son1 are nodes in the tree
    public static boolean areBrothers(BinNode<Integer> tr, BinNode<Integer> son1, BinNode<Integer> son2)//Q29
    {
        if (tr == null || son1 == null || son2 == null)
            return false;
        if (tr.getLeft() == son1 && tr.getRight() == son2)
            return true;
        if (tr.getLeft() == son2 && tr.getRight() == son1)
            return true;
        return areBrothers(tr.getLeft(), son1, son2) || areBrothers(tr.getRight(), son1, son2);
    }


    //The operation accepts a binary tree and two values and returns
    //'True' if y is a descendant of x', false' - otherwise.
    public static boolean isDescendent(BinNode<Integer> tr, int x, int y)//Q30
    {
        if (tr == null)
            return false;
        if (tr.getValue() == x)
            return isDescendent(tr.getLeft(), x, y) || isDescendent(tr.getRight(), x, y);
        if (tr.getValue() == y)
            return true;
        return isDescendent(tr.getLeft(), x, y) || isDescendent(tr.getRight(), x, y);
    }

    //The operation accepts a binary tree and two nodes
    //and returns 'true' if node2 is a child of node1,
    //'false' - otherwise.
    public static boolean isDescendent(BinNode<Integer> tr, BinNode<Integer> node1, BinNode<Integer> node2)//Q31
    {
        if (tr == null || node1 == null || node2 == null)
            return false;
        if (tr == node1)
            return tr.getLeft() == node2 || tr.getRight() == node2;
        return isDescendent(tr.getLeft(), node1, node2) || isDescendent(tr.getRight(), node1, node2);
    }


    //The operation returns a first ancestor of a second
    //Nodes in the tree. null – if one of the nodes is
    //The root or one of the trees is empty

    public static BinNode<Integer> commonAncestor(BinNode<Integer> tr, BinNode<Integer> s1, BinNode<Integer> s2)//Q32
    {
        if (tr == null || s1 == null || s2 == null)
            return null;
        if (tr == s1 || tr == s2)
            return tr;
        BinNode<Integer> left = commonAncestor(tr.getLeft(), s1, s2);
        BinNode<Integer> right = commonAncestor(tr.getRight(), s1, s2);
        if (left != null && right != null)
            return tr;
        if (left != null)
            return left;
        return right;
    }


    //An operation that accepts a binary-tree node in the tree and returns its level.
    //Assumption: the tree is not empty and a node exists in the tree.
    public static int level(BinNode<Integer> tr, BinNode<Integer> node)//Q33
    {
        if (tr == null || node == null)
            return -1;
        if (tr == node)
            return 0;
        int left = level(tr.getLeft(), node);
        if (left != -1)
            return left + 1;
        int right = level(tr.getRight(), node);
        if (right != -1)
            return right + 1;
        return -1;
    }


    //An operation that receives 2 binary trees and returns 'true' if they are similar, 'false' - otherwise.
    public static boolean similar(BinNode<Integer> tr1, BinNode<Integer> tr2)//Q34
    {
        if (tr1 == null && tr2 == null)
            return true;
        if (tr1 == null || tr2 == null)
            return false;
        return similar(tr1.getLeft(), tr2.getLeft()) && similar(tr1.getRight(), tr2.getRight());
    }

    //An operation that receives 2 binary trees and returns 'true' if they are the same, 'false' - otherwise
    public static boolean equal(BinNode<Integer> tr1, BinNode<Integer> tr2)//Q35
    {
        if (tr1 == null && tr2 == null)
            return true;
        if (tr1 == null || tr2 == null)
            return false;
        if (!tr1.getValue().equals(tr2.getValue()))
            return false;
        return equal(tr1.getLeft(), tr2.getLeft()) && equal(tr1.getRight(), tr2.getRight());
    }


    //An operation that receives 2 trees tr2,tr1 and returns 'true' if all the values of tr1 are in tr2, 'false' - otherwise.
    public static boolean allTr1InTr2(BinNode<Integer> tr1, BinNode<Integer> tr2)
    {
        if (tr1 == null)
            return true;
        if (tr2 == null)
            return false;
        if (tr1.getValue().equals(tr2.getValue()))
            return allTr1InTr2(tr1.getLeft(), tr2.getLeft()) && allTr1InTr2(tr1.getRight(), tr2.getRight());
        return allTr1InTr2(tr1, tr2.getLeft()) || allTr1InTr2(tr1, tr2.getRight());
    }

}

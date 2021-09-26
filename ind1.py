#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    A = {"a", "d", "k", "l", "o", "s"}
    B = {"d", "e", "k", "s", "u", "x"}
    C = {"o", "p", "w"}
    D = {"d", "n", "r", "y", "z"}

    ab1 = A.difference(B)
    cd1 = A.intersection(B)
    X = ab1.union(cd1)
    # X = (A.difference(B)).union(A.intersection(B))
    print(f"X = {X}")

    na = u.difference(A)
    nb = u.difference(B)
    ab2 = na.intersection(nb)
    cd2 = C.union(D)
    Y = ab2.difference(cd2)
    # Y = (na.intersection(nb)).difference(C.union(D))

    print(f"Y = {Y}")

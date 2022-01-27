def search_fuzzy(P, q):
    """
    The function serach phrases in the a single query
    
    Input:
     P : List[List[str]] - list with phrases, the phrases string are splited into list
     q : string - a string with the current sentense
    
    Output:
     output: List[str] - list with the matching phrases
    """
    # create a dict pointing to index
    q_split = q.split()
    n_q_words = len(q_split)
    q_dict = {}
    for i, x in enumerate(q_split):
        if x in q_dict:
            q_dict[x].append(i)
        else:
            q_dict[x] = [i]

    output = []
    for p_split in P:
        n_s = len(p_split)
        p_idx = []
        if p_split[0] in q_dict:
            # lock for match with max one word difference
            for first_idx in q_dict[p_split[0]]:
                is_match = True
                is_jumped = False  # mark if already one word was skip
                ip = 1
                iq = first_idx + 1
                while (ip < n_s) and (iq < first_idx + n_s + 1):
                    if p_split[ip] == q_split[iq]:
                        ip += 1
                        iq += 1
                    elif (not is_jumped) and (iq + 1 < n_q_words) and (p_split[ip] == q_split[iq + 1]):
                        is_jumped = True
                        ip += 1
                        iq += 2
                    else:
                        is_match = False
                        break

                # if fuzzy matched add to output
                if is_match:
                    output.append(" ".join(q_split[first_idx:iq]))

    return output


def phrasel_search(P, Queries):
    P_split = [x.split() for x in P]
    ans = []
    for q in Queries:
        a = search_fuzzy(P_split, q)
        ans.append(a)
    return ans


def check_solution(returned_ans, solution):
    """
    Help function to compare the given solution 
    with the algorithm result.
    Not part of the question!
    """
    if len(returned_ans) != len(solution):
        print("the solution has {} entries, but should have {}".format(
            len(solution), len(returned_ans)))
        return False

    for i in range(len(returned_ans)):
        if set(returned_ans[i]).difference(set(solution[i])):
            print("solution does not match")
            return False

    return True


if __name__ == "__main__":
    file_name = "smaple.json"
    with open(file_name, 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')
        #if check_solution(returned_ans, sample_data['solution']):
        #    print("solution matches the returned answer")


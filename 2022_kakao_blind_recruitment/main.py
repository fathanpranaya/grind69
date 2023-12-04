def solution(id_list, report, k):
    # generate dic of reported user
    reported_db = {key: [] for key in id_list}
    reporter_cnt = {key: 0 for key in id_list}

    # iterate report and added to reported dict
    for e in report:
        reporter, reported = e.split(" ")
        # append reporter to the reported_db
        if reporter not in reported_db.get(reported):
            reported_db.get(reported).append(reporter)
        
    for id in id_list:
        # suspend case:
        # if the len of val is more than equal k: suspended, add counter to reporter_cnt
        if len(reported_db.get(id)) >= k:
            for reporter_id in reported_db.get(id):
                reporter_cnt[reporter_id] += 1

    return list(reporter_cnt.values())

if __name__ == "__main__":
    # id_list = ["muzi", "frodo", "apeach", "neo"]
    # report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    # k = 2

    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3
    print(solution(id_list, report, k))
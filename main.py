import controller
import jadge_exam


def main():
    controllers = controller.Controller()
    jadge = jadge_exam.Jadge_exam()
    # 生徒情報の読み込み
    controllers.read_student_information()
    # 生徒の点数入力
    controllers.enter_exam(controllers.student_list)
    # 生徒のクラスの判断
    jadge.jadge_exam(controllers.student_list, controllers.exam_list)
    # 生徒のクラス分け
    controllers.division_class()
    # 結果発表
    controllers.show_result(controllers.science_member_list, controllers.literature_member_list, controllers.failure_list)

main()
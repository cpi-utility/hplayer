import cv2
import sys

def play_video(video_path):
    # Открыть видеофайл
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Ошибка при открытии видеофайла")
        return

    # Определение кодека и параметров видео
    codec = cv2.VideoWriter_fourcc(*'HEVC')  # Кодек HEVC
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Создание окна для воспроизведения
    cv2.namedWindow('HEVC Video Player', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('HEVC Video Player', width, height)

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            # Показать кадр
            cv2.imshow('HEVC Video Player', frame)

            # Пауза между кадрами, управление скоростью воспроизведения
            if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
                break
        else:
            break

    # Очистка
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python video_player.py <путь_к_видео>")
        sys.exit(1)

    video_path = sys.argv[1]
    play_video(video_path)
